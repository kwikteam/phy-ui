# -*- coding: utf-8 -*-

"""Cluster store."""

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

import os.path as op
from collections import defaultdict

from ...ext.six import string_types


#------------------------------------------------------------------------------
# Data stores
#------------------------------------------------------------------------------

class MemoryStore(object):
    """Store cluster-related data in memory."""
    def __init__(self):
        self._ds = {}

    def store(self, cluster, **data):
        """Store cluster-related data."""
        if cluster not in self._ds:
            self._ds[cluster] = {}
        self._ds[cluster].update(data)

    def load(self, cluster, keys=None):
        """Load cluster-related data."""
        if keys is None:
            return self._ds.get(cluster, {})
        else:
            if isinstance(keys, string_types):
                return self._ds.get(cluster, {}).get(keys, None)
            assert isinstance(keys, list)
            return {key: self._ds.get(cluster, {}).get(key, None)
                    for key in keys}

    def keys(self):
        """List of cluster ids in the store."""
        return sorted(self._ds.keys())

    def delete(self, clusters):
        """Delete some clusters from the store."""
        assert isinstance(clusters, list)
        for cluster in clusters:
            if cluster in self._ds:
                del self._ds[cluster]


class DiskStore(object):
    """Store cluster-related data on disk."""
    def __init__(self, directory):
        self._directory = op.realpath(directory)

    def _path(self, rel_path):
        """Return the absolute path of a relative path in the disk store."""
        return op.realpath(op.join(self._directory, rel_path))

    def store(self, cluster, **data):
        """Store cluster-related data."""

    def load(self, cluster, keys=None):
        """Load cluster-related data."""

    def keys(self):
        """List of cluster ids in the store."""

    def delete(self, clusters):
        """Delete some clusters from the store."""