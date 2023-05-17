import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main():
    mutation_data = pd.read_csv("mutation_data.csv")
    print(mutation_data.head())
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(mutation_data.describe())
    sb.pairplot(mutation_data.dropna(), hue='Gender')
    plt.show()

main()