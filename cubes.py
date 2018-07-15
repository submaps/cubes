import itertools
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D


def get_cube_proba(n, s):
    # 1,..,6
    # 1,..,6
    # ...
    # 1,..,6
    # s_total = sum(cube_value1+cube_value2+...) = 6^n/n
    # s = k_s/N_s
    all_possible_cubes = list(itertools.product(range(1, 7), repeat=n))
    assert len(all_possible_cubes) == 6 ** n
    all_possible_sumes = [sum(items) for items in all_possible_cubes]
    # count = get_counter_gl(n, s, all_possible_cubes)
    # print(counter)
    counter = Counter(all_possible_sumes)
    count = counter[s]
    # count = all_possible_sumes.count(s)
    K = count
    N = 6 ** n
    P = K / N
    return count, P

if __name__ == '__main__':
    # есть N игральных кубиков с 6 сторонами
    # напишите функцию которая для заданного кол-ва
    # кубиков n и заданной суммы s выводит вероятность выпадения этой суммы
    pn_list = []
    n_list = range(1, 6)
    sn_list = range(1, 61)

    total_list = []
    for n in n_list:
        print("total combinations", 6 ** n)
        p_list = []
        # score_list = range(n, 6*n)
        score_list = sn_list
        for s in score_list:
            count, p = get_cube_proba(n, s)
            # print(s, count, p)
            p_list.append(p)
            pn_list.append(p)
            total_list.append([n, s, p])

        max_p = max(p_list)
        max_e = score_list[p_list.index(max_p)]
        print("max element:", score_list[p_list.index(max_p)], max_p)
        print(min(p_list), np.mean(p_list), max(p_list))

        plt.figure()
        plt.plot(score_list, p_list)
        plt.title("Probability distribution n={}\n e:{} p:{:.3f}".format(n, max_e, max_p))
        plt.xlabel("sum")
        plt.ylabel("p")
        plt.savefig("img/cube_pdf_{}.png".format(n))
        # plt.show()
        plt.close()

    fig = plt.figure()
    ax = Axes3D(fig)
    narr, sarr, parr = np.array(total_list).T
    ax.bar3d(narr, sarr, parr, 1, 1, 0.02)

    ax.set_xlabel("n")
    ax.set_ylabel("s")
    ax.set_zlabel("p")
    # plt.savefig("img/cube3d.png")
    plt.show()
