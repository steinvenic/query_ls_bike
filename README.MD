# 获取链尚自行车站点信息

## 1）配置

- `pip install -r requirements.txt`

- 查询自己所在区的经纬度，对应`latitude`和`longitude`

- `python main.py`

  



## 2)使用

- 获取该区域所有站点信息：`http://127.0.0.1:3212/4f5635c9-5a5e-4b17-8b4d-68d3b3d87c5a?my_stName=all`

- 根据站点名查询：`http://127.0.0.1:3212/4f5635c9-5a5e-4b17-8b4d-68d3b3d87c5a?my_stName=光明路`

  ```
  [
    {
      "bikeNum": 19,
      "cityId": 4,
      "iconPath": "/Images/st_mark.png",
      "id": 93,
      "latitude": 31.296238,
      "lockEmptyNum": 11,
      "longitude": 121.117373,
      "stName": "轻轨光明路站北",
      "totalNum": 30
    },
    {
      "bikeNum": 24,
      "cityId": 4,
      "iconPath": "/Images/st_mark.png",
      "id": 94,
      "latitude": 31.296075,
      "lockEmptyNum": 6,
      "longitude": 121.117399,
      "stName": "轻轨光明路站南",
      "totalNum": 30
    }
  ]
  ```

  