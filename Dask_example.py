import dask.array as da
import numpy as np
import time

# Create a NumPy array
data = np.random.rand(1000000)

# Time a sequential calculation (using NumPy)
start_time = time.time()
result_serial = data * 2  # Double all elements
serial_time = time.time() - start_time

# Create a Dask array
dask_array = da.from_array(data, chunks=(10000,))  # Split data into chunks

# Time a parallel calculation (using Dask)
start_time = time.time()
result_parallel = dask_array * 2
result_parallel = result_parallel.compute()  # Trigger the parallel execution
parallel_time = time.time() - start_time

# Print the results and execution times
print("Serial result:", result_serial[0])
print("Parallel result:", result_parallel[0])
print("Serial time:", serial_time, "seconds")
print("Parallel time:", parallel_time, "seconds")
##