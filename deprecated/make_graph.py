import matplotlib.pyplot as plt


def bar_plot(x1=None, y1=None, x2=None, y2=None, title="Plot"):
    # cases.plot(x='Specimen date',y='Cumulative lab-confirmed cases',color='green')
    # deaths.plot(x='Reporting date',y='Cumulative deaths',color='red')
    # plt.figure(title, figsize=[12,4])
    # plt.autoscale(tight=True)
    # ax = plt.gca()
    # plt.plot(kind='bar', x=x1, y=y1,ax=ax, color='green')
    # plt.plot(kind='bar', x=x2, y=y2, ax=ax, color='red')
    # plt.subplots_adjust(left=0.06,bottom=0.31,right=0.99,top=0.98)
    # plt.xticks(fontsize=8)
    # plt.show()
    plt.figure(title, figsize=[12, 4])
    plt.autoscale(tight=True)
    ax = plt.gca()
    ax.bar(x1, y1)
    ax.bar(x2, y2)
    plt.show()
