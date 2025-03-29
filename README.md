# Route_optimization_using_Hybrid-Algorithm-
INTRODUCTION  
              Real-time adaptive navigation in urban areas is 
increasingly critical area of research, especially with the 
rise of smart cities and  autonomous vehicles. Traditional 
navigation systems Often relies on static maps or periodic 
traffic updates, which can result in suboptimal route 
decision when traffic conditions fluctuate rapidly. To 
address this, study explores a stimulation of framework 
that dynamicaly adjusts routes based on real-time traffic 
data, aiming to optimize , travel times in complex urban 
environments. Using Manhattan, New York as a case 
study ,it leverages OpenStreetMap (OSM) data to 
construct comprehensive graph of the city’s road 
network, enabling realistic stimulations. 
  The approach combines the A* pathfinding 
algorithm with a traffic-aware cost function, allowing 
system to make efficient routing decisions based on both 
distance and anticipated travel delays. The heuristic 
components of A* modified to estimate travel time more 
accurately by incorporating traffic factors, simulating real
world conditions. To further enhance capabilities , the 
study stimulate traffic changes through periodic updates 
to edge weights, reflecting fluctuating rosd congestion 
levels. 

EXPERIMENTS AND RESULTS 
    Series of simulation experiment had conducted 
to evaluate the performance of the proposed pathfinding 
framework under varying traffic condition. For each 
experiment, a vehicle begins at a predefined start node in 
Manhattan’s road network and progress towards a target 
destination. The frame work records the initial route and 
updates periodically based on newly simulated traffic data. 
• ROUTE ADAPTALITY 
                 The results indicates that adaptive routing provides     
Significant improvements in travel time under fluctuating       
traffic . The A* algorithm with traffic-sensitive heuristic 
consistently adapted routes in response to new traffic data, 
reducing the delays compared to static pathfinding methods. 
• IMPACT OF UPDATED INTERVALS 
                  This study evaluates the effect of various update 
intervals (2,5,10 seconds) on travell efficiency.shorter update 
intervals improved adaptability but increased computional 
demands. For urban networks with moderate traffic, a 5 
second interval achieved a balanced between responsiveness 
and computational effieciency.
Steps to Run the code.
step 1:  clone the repository.
          git clone "https://github.com/GDking08/Route_optimization_using_Hybrid-Algorithm'
step 2: cd Route_optimization_using_Hybrid-Algorithm
step 3: pip install -r requirements.txt
step 4: run main.py
After successfull executin the html file "route_map" in this diirectory.
click this html to see the route.

