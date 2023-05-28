import time

start_time = time.process_time()

# Đo thời gian thực hiện một số công việc
sum([i**2 for i in range(100000)])

end_time = time.process_time()

result = end_time - start_time

print("thoi gian o CPU: ", result)