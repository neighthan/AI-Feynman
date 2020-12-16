"""Remove an input neuron from a NN."""

import numpy as np
import torch
import torch.nn as nn

is_cuda = torch.cuda.is_available()


def remove_input_neuron(net, n_inp, idx_neuron, ct_median, save_filename):
    removed_weights = net.linear1.weight[:, idx_neuron]
    # Remove the weights associated with the removed input neuron
    t = torch.transpose(net.linear1.weight, 0, 1)
    preserved_ids = torch.LongTensor(
        np.array(list(set(range(n_inp)) - set([idx_neuron])))
    )
    t = nn.Parameter(t[preserved_ids, :])
    net.linear1.weight = nn.Parameter(torch.transpose(t, 0, 1))
    # Adjust the biases
    net.linear1.bias.data += ct_median * removed_weights
    torch.save(net.state_dict(), save_filename)
