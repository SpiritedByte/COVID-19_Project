import matplotlib.pyplot as plt

def plot(cases,deaths):
    cases.plot(x='Specimen date',y='Cumulative lab-confirmed cases',color='green')
    deaths.plot(x='Reporting date',y='Cumulative deaths',color='red')
    plt.show()