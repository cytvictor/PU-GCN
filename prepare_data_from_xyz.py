import h5py
import sys
import numpy as np

def read_xyz(xyz_dir, batch_size=256):
    
    with open(xyz_dir, 'r') as xyzf:
        content = xyzf.read()
        xyzf.close()
    i = 0
    
    dat = np.ndarray(shape=(0, batch_size, 3))
    i = 0
    batch_data = np.zeros(shape=(0,3))
    for line in content.splitlines():
        i += 1
        batch_data = np.append(batch_data, [[float(x) for x in line.split(' ')]], axis=0)
        if i % batch_size == 0:
            dat = np.append(dat, [batch_data], axis=0)
            print("append", len(dat), len(batch_data))
            batch_data = np.zeros(shape=(0,3))
    return dat

if __name__ == "__main__":
    input_data = read_xyz(sys.argv[1], 256)
    gt_data = read_xyz(sys.argv[2], 1024)
    out_filepath = sys.argv[1] + ".h5"
    f = h5py.File(out_filepath, "w")
    f.create_dataset("test_256", data=input_data)
    f.create_dataset("test_1024", data=gt_data)

    
