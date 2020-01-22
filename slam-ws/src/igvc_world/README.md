## IGVC Basic Course Gazebo Simulation

1. Install the models into the gazebo models folder.
 - `cd ~/SLAM/slam-ws/src/igvc_world/models`
 - `./install_models.sh`
2. Build src
 - `cd ~/SLAM/slam-ws`
 - `catkin_make`
3. Launch world in gazebo
 - `gazebo ~/SLAM/slam-ws/src/igvc_world/worlds/igvc_basic.world`
4. Launch caffeine in this world
 - `roslaunch caffeine caffeine_gazebo.launch world:="ABSOLUTE_PATH_TO_WORLD_FILE"`
