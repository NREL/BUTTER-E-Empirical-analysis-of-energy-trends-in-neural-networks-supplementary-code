## Constants

bytes_per_float = 4  # 32-bit single-precision floats

# 2 x Intel® Xeon® Gold 6154 Processor
# L3 Cache	24.75 MB, non-inclusive of L2
# L2 Cache 1MB / Core inclusive of L1
# L1 Cache 32KB D, 32KB I/ Core
num_sockets = 2
cores_per_socket = 18

cpu_total_cores = num_sockets * cores_per_socket

cpu_level_1_bytes_per_core = 32 * 1024
cpu_level_1_bytes_per_socket = cpu_level_1_bytes_per_core * cores_per_socket
cpu_level_1_bytes = cpu_level_1_bytes_per_socket * num_sockets


cpu_level_2_bytes_per_core = 1 * 1024 * 1024
cpu_level_2_bytes_per_socket = cpu_level_2_bytes_per_core * cores_per_socket
cpu_level_2_bytes = cpu_level_2_bytes_per_socket * num_sockets

cpu_level_3_bytes_per_socket = 24.75 * 1024 * 1024
cpu_level_3_bytes = cpu_level_3_bytes_per_socket * num_sockets

cpu_total_cache_bytes_per_socket = (
    cpu_level_2_bytes_per_socket + cpu_level_3_bytes_per_socket
)
cpu_total_cache_bytes = cpu_total_cache_bytes_per_socket * num_sockets

bytes_per_parameter = 4 * (3 + 256)


def size_to_bytes(size):
    return size * bytes_per_parameter


def bytes_to_size(bytes):
    return bytes / (bytes_per_parameter)


bytes_per_float = 4  # 32-bit single-precision floats

# 2x V100
#
num_gpus = 2

sms_per_gpu = 84

gpu_total_sms = num_gpus * sms_per_gpu

gpu_level_1_bytes_per_sm = (128 - 16) * 1024
gpu_level_1_bytes_per_gpu = gpu_level_1_bytes_per_sm * sms_per_gpu
gpu_level_1_bytes = gpu_level_1_bytes_per_gpu * num_gpus

gpu_level_2_bytes_per_gpu = 6144 * 1024
gpu_level_2_bytes = gpu_level_2_bytes_per_gpu * num_gpus

gpu_ram_bytes_per_gpu = 16 * (1024**3)
gpu_ram_bytes = gpu_ram_bytes_per_gpu * num_gpus


system_ram_bytes = 96 * 2**30
socket_ram_bytes = system_ram_bytes / num_sockets

cpu_caches = [
    # (0, cpu_register_file_size, cores_per_socket*num_sockets),
    (1, cpu_level_1_bytes_per_core, cores_per_socket * num_sockets),
    (2, cpu_level_2_bytes_per_core, cores_per_socket * num_sockets),
    (3, cpu_level_3_bytes_per_socket, num_sockets),
    # (5, socket_ram_bytes, num_sockets),
    (4, system_ram_bytes, 1),
]

gpu_caches = [
    (1, gpu_level_1_bytes_per_sm, sms_per_gpu * num_gpus),
    (2, gpu_level_2_bytes_per_gpu, num_gpus),
    (3, gpu_ram_bytes_per_gpu, num_gpus),
    # (5, socket_ram_bytes, num_sockets),
    # (6, system_ram_bytes, 1),
]

num_caching_levels = max(len(cpu_caches), len(gpu_caches))

cpu_cache_sizes = [e[1] for e in cpu_caches]
gpu_cache_sizes = [e[1] for e in gpu_caches]


### Colors

pallette = [
    ["#9530E6", "#D732CE", "#DF3858", "#EE723B", "#EEBF00"],
    ["#f5b9c0", "#ed95a0", "#df3858", "#c62b46", "#ad1e35"],
    ["#c0b9f5", "#a095ed", "#5838df", "#462bc6", "#351ead"],
    ["#008d89", "#00b8b3", "#ed95a0", "#df3858", "#ad1e35"],
    ["#051cb2", "#0a34df", "#df3858", "#4dc708", "#2C9B03"],
]
cpu_color = pallette[-1][0]
gpu_color = pallette[-1][-1]


working_set_colors = [
    pallette[0][0],
    pallette[3][0],
    pallette[0][3],
    pallette[0][2],
]

working_set_labels = [
    "Inter-layer maximum, $l$",
    "Forward pass, $f$ ",
    "Backward pass, $b$ ",
    "Dataset, $d$ ",
]

cache_colors = [
    "darkred",
    "darkblue",
    "darkgreen",
]
