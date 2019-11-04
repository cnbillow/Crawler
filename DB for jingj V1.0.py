import time

import requests, json

"""爬取豆瓣网的电影名称、评分"""


class Douban:
    def __init__(self, tag, num):
        self.tag = tag
        self.num = num
        self.url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%s&sort=rank&' \
                   'page_limit=%s&page_start=0' % (self.tag, self.num)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }

    # 解析数据
    def parse_data(self):
        res = requests.get(url=self.url, headers=self.headers)
        dic_data = json.loads(res.content.decode())
        new_dict = {}
        for index in range(self.num):
            dic_data_deep = dic_data["subjects"][index]
            new_dict[index] = [dic_data_deep.get('title'), dic_data_deep.get('rate'), dic_data_deep.get('url')]
        return new_dict

    # 冒泡排序
    def sort(self, new_dict):
        for i in range(self.num):
            for j in range(self.num - i - 1):
                if new_dict[j][1] < new_dict[j + 1][1]:
                    new_dict[j], new_dict[j + 1] = new_dict[j + 1], new_dict[j]
        return new_dict

    # 保存到文件
    def save(self, data):
        f = open('C:/Users/ZHY/Desktop/Movie_%s.txt' % self.tag, 'w+')
        for i in range(self.num):
            sig_data = data[i]
            f.write('%d.' % (i + 1) + str(sig_data) + '\n')
        f.close()

    def main(self):
        # 构建请求头和url
        # 发送请求，获取数据
        # 解析数据
        new_dict = self.parse_data()
        # print(new_dict)
        final_dict = self.sort(new_dict)
        # print(final_dict)
        # 保存到文件
        self.save(final_dict)
        print("文件已保存到桌面，静静么么哒~")


if __name__ == '__main__':
    tag = input("请输入电影类型（华语/欧美/韩国/日本/动作/喜剧/爱情/科幻/悬疑/恐怖/成长）：")
    num = input("请输入电影数（默认100）：")
    if num == '':
        num = 100
    else:
        num = int(num)
    douban = Douban(tag, num)
    douban.main()
    time.sleep(60)
