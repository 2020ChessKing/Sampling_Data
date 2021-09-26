#   imports
import  plotly.express as plotly, plotly.figure_factory as graphs, plotly.graph_objects as graphObjects
import pandas as panda, statistics as stats, random


#   code

# raw materals
data_frame = panda.read_csv('C:\Swarup\WhiteHat Jr\Python\Projects\Sampling_Data\medium_data.csv')
data = data_frame["claps"].tolist()
clap_data_mean_list = []

# functions
def setup():
    for i in range(0, 20):
        sample_data = sampleData()
        clap_data_mean_list.append(sample_data)

    dist_plot = graphs.create_distplot([clap_data_mean_list], ["Claps"], show_hist=False)
    dist_plot.show()

    mean_clap_sampled = stats.mean(clap_data_mean_list)
    mean_clap_population = stats.mean(data)
    print("The mean of the sample means is: ", mean_clap_sampled, "-- -- -- The mean of the population is: ", mean_clap_population)



def sampleData():
    clap_data_list = []

    for i in range(0, 30):
        random_number = random.randint(1, len(data)-1)
        random_clap = round(data[random_number])
        clap_data_list.append(random_clap)

    clap_data_list_mean = stats.mean(clap_data_list)
    return round(clap_data_list_mean)



def showGraph():
    dist_plot = graphs.create_distplot([clap_data_mean_list], ["claps"], show_hist=False)
    dist_plot.show()



if __name__ == "__main__":
    setup()