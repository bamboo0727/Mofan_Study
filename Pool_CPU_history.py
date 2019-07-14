
import multiprocessing as mp

def job(x):
    return x*x


def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(100000))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(100000)]
    # 从迭代器中取出
    print([res1.get() for res1 in multi_res])

if __name__ == '__main__':
    multicore()
