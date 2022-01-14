### Veloparser

Veloparser is a simple application which does following:

- Supports just Velodyne VLP16 at the moment.
- Takes a pcap file recorded by Velodyne lidar as input.
- Extracts all Frames from the pcap file.
- Saves both data-frames and position-frames.
- __Data frames__ are saved as __Point Clouds (.pcd)__ and/or as __plain Text-File__. 
- __Position frames__ are saved only as __Text-File__
- Converts frame's timestamps to GPS Week of Second format for synchronization with IMU/GNSS devices
- Can be parameterizes by yaml file.


##### Environment

```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```
```
$ conda create -n lidar-analysis python=3.8 -y
$ conda activate lidar-analysis
```


##### Dependencies

```
$ pip install -r requirements.txt
```


##### Usage

```
$ python main.py -p ../../data/raw_pcap/vlp16.pcap -o ../../data/pcd_txt -c params.yaml
```


##### Output

Below a sample out of 2 Points in a __point cloud file__

``
Time [musec], X [m], Y [m], Z [m], ID, Intensity, Latitude [Deg], Longitudes [Deg], Distance [m]
2795827803, 0.032293, 5.781942, -1.549291, 0, 6, 0.320, -15.000, 5.986
2795827806, 0.083565, 14.399564, 0.251350, 1, 6, 0.333, 1.000, 14.402
``

All __Point Cloud__ PCD-Files have follwoing fields:

1) X-Coordinate
2) Y-Coordinate
3) Z-Coordinate
4) Intensity
