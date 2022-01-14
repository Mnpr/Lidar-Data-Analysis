# Lidar Data Analysis

**Raw Input**

Velodyne Puck Capture (`x.pcap`)

**Modules**

- [ ] [[Data Preprocessing](./data_preprocessing/)]
- [ ] [[Data Formatting](./data_formatting/)]
- [ ] [[Data Annotation](./data_annotation/)]
- [ ] [[Data Loaders ](./data_loaders)]
- [ ] [[ROS Modules](./ros2/)]

**Information Flow**

![](./assets/data_processing_n_annotation.png)

**Output**

- KITTI format compatible Lidar format : (`x.bin`)
- Annotation files: (`subset_of_x.pcd`)

**References**

1. https://gitlab.com/jimquery/pcap-parse/-/tree/master
2. https://gist.github.com/SebastianGrans/6ae5cab66e453a14a859b66cd9579239
3. https://github.com/ArashJavan/veloparser
4. https://github.com/hitxing/Lidar-data-decode/