# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

"""Local MAAS system site configuration."""

site_configuration = {
    "systems": [
        {
            "name": "local-maas",
            "descr": "Local MAAS system test deployment cluster",
            "hostnames": [],
            "modules_system": "nomod",
            "partitions": [
                {
                    "name": "login",
                    "descr": "Cluster login nodes",
                    "launcher": "local",
                    "environs": ["builtin"],
                    "scheduler": "local",
                },
                {
                    "name": "compute-mpi",
                    "descr": "200Gbps RDMA-enabled partition",
                    "launcher": "mpirun",
                    "env_vars": [["UCX_NET_DEVICES", "mlx5_3:1"]],
                    "environs": ["builtin", "mpi-gnu"],
                    "access": ["--partition=compute-mpi"],
                    "scheduler": "slurm",
                    "time_limit": "1h",
                    "max_jobs": 100,
                },
                {
                    "name": "compute-gpu",
                    "descr": "NVIDIA L40 GPU-equipped partition",
                    "launcher": "local",
                    "environs": ["builtin", "cuda"],
                    "access": ["--partition=compute-gpu", "--gres=gpu:1"],
                    "scheduler": "slurm",
                    "time_limit": "1h",
                    "max_jobs": 100,
                },
            ],
        },
    ],  # end of systems
    "environments": [
        {
            "name": "cuda",
            "cc": "nvcc",
            "cxx": "nvcc",
            "target_systems": ["local-maas"],
            "features": ["cuda"],
        },
        {
            "name": "mpi-gnu",
            "cc": "mpicc",
            "cxx": "mpicxx",
            "ftn": "mpif90",
            "target_systems": ["local-maas"],
            "features": ["mpi"],
        },
        {
            "name": "builtin",
            "cc": "cc",
            "cxx": "CC",
            "ftn": "ftn",
            "target_systems": ["local-maas"],
        },
    ],  # end of environments
}
