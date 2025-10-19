import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

my_last_digit = 2

# ช่วงของการแจกแจง
a = my_last_digit - 5
b = my_last_digit + 5

# สร้างตัวแปรสุ่ม X
random_data = np.random.uniform(a, b, 1000)

# คำนวณค่าทางทฤษฎี
theo_mean = (a + b) / 2
theo_std = np.sqrt((b - a) ** 2 / 12)

print(f"Theoretical mean: {theo_mean}")
print(f"Theoretical std: {theo_std}")

# คำนวณค่าจากตัวแปรสุ่ม X
sim_mean = np.mean(random_data)
sim_std = np.std(random_data)

print(f"Simulated Mean: {sim_mean}")
print(f"Simulated Std: {sim_std}")

# สร้าง sample 3 ขนาด
sample_sizes = [10, 40, 100]


plt.figure(figsize=(12, 8))
all_sample_means = []

for i, n in enumerate(sample_sizes, 1):
    # สุ่ทข้อมูลมา n ค่าหาค่าเฉลี่ย ทำซ้ำทั้งหมด 1000 รอบ
    sample_means = [np.mean(np.random.uniform(a, b, n)) for _ in range(1000)]
    all_sample_means.append(sample_means)

    plt.subplot(3, 1, i)
    plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f"Sample (n={n})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.xlim(a, b)
    plt.ylim(0, 200)

plt.tight_layout()
plt.show()



# Mean
mean_n10 = np.mean(all_sample_means[0])
mean_n40 = np.mean(all_sample_means[1])
mean_n100 = np.mean(all_sample_means[2])

# Std
std_n10 = np.sqrt(np.var(all_sample_means[0]))
std_n40 = np.sqrt(np.var(all_sample_means[1]))
std_n100 = np.sqrt(np.var(all_sample_means[2]))

# theo Std
theo_std_n10 = theo_std / np.sqrt(10)
theo_std_n40 = theo_std / np.sqrt(40)
theo_std_n100 = theo_std / np.sqrt(100)

print(f"\n---------------------")
print(f"n = 10")
print(f"Mean = {mean_n10}")
print(f"Std = {std_n10}")
print(f"Theo Std = {theo_std_n10}")

print(f"---------------------")
print(f"n = 40")
print(f"Mean = {mean_n40}")
print(f"Std = {std_n40}")
print(f"Theo Std = {theo_std_n40}")

print(f"---------------------")
print(f"n = 100")
print(f"Mean = {mean_n100}")
print(f"Std = {std_n100}")
print(f"Theo Std = {theo_std_n100}")


