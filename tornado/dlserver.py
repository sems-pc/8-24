import tornado.ioloop
import tornado.web
import os
import datetime


class MainHandler(tornado.web.RequestHandler):  # 服务器应用程序主体
    def get(self):
        self.render("downloads/index.html")  # 加载网页文件
        ua = self.request.headers['User-Agent']
        time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(time, ua)  # 可以查看每次启动的User-Agent（如果没有下面三行代码，记录会在重启服务器后会丢失）
        with open('server.log', "a+") as f:
            f.write(time + " " + ua + "\n")
            f.close()


def make_app():  # 生成应用配置
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
        static_path=os.path.join(os.path.dirname(__file__), "downloads")  # 静态化可以防止浏览器无法加载Tornado服务器上的JavaScript文件
    )


if __name__ == "__main__":  # 启动服务器程序
    try:
        app = make_app()
        app.listen(100)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
