import requests
import re
import os
# 爬取豆瓣网/豆瓣电影 Top 250，下载图片，图片名为：排行+电影名

# 获取网站html
for num in range(0, 226, 25):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(num)
    html = requests.get(url=url)

# 提取信息
    pattern = re.compile(r'<li>.*?<em class="">(\d*)</em>.*?alt="([^"]*?)".*?src="(.*?)".*?</li>', re.S)
    # bug:少了几张图片 原因：(\w*?) 匹配不到(蝙蝠侠：黑夜骑士)  改正：([^"]*?)
    pattern_list = re.findall(pattern, html.text)
    print(pattern_list)
    print(len(pattern_list))
# 保存信息
    path = 'E:/豆瓣Top 250/'
    if not os.path.exists(path):
        os.mkdir(path)

    for movie in pattern_list:
        pic_name = movie[0] + ' ' + movie[1] + '.jpg'
        # BUG:保存的文件名只有movie[0]  改正： ':'改成' '
        path_pic = path + pic_name
        if not os.path.exists(path_pic):
            pic = requests.get(movie[2])
            with open(path_pic, 'wb') as file:
                file.write(pic.content)
                print('图片已下载成功')
        else:
            print('文件已存在')

