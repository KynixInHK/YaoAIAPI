# YaoAI(苏乐瑶/Yuki)
<p style="text-indent: 2em">
    苏乐瑶（Yuki）是普萘洛尔生态下人工智能伙伴，中文名字是“苏乐瑶”，昵称“瑶瑶”，英文名字“Yuki”。是由自由开发者Kynix基于浪潮发布的大型中文预训练模型“源1.0”开发而来，对源1.0提供的接口进行了高级封装，使用flask框架使其拥有了在网际网络上提供API服务的能力。
</p>

## 基于YaoAI进行的二次开发
### 环境需求
- Python >= 3.6
- pip > 20.2.2
### 1. 克隆项目
```shell
$ git clone https://github.com/KynixInHK/YaoAIAPI.git
```
### 2. 安装依赖
```shell
$ cd YaoAIAPI
$ pip install -r requirements.txt
```
### 3.添加必要信息
#### 数据库信息
打开/static/database.json，其中的内容应当如下所示：
```json
{
    "url": "yoururl",
    "port": "port",
    "user": "username",
    "password": "yourpassword",
    "database": "databasename"
}
```
各字段含义如下：
- url：数据库的IP地址
- port：数据库的端口号
- user：连接数据库的用户名
- password：连接数据库的密码
- database：YaoAI的数据库
#### 源1.0 API使用许可
源1.0的API使用许可由浪潮信息提供，需要开发人员自行申请使用。官网是<a href="https://air.inspur.com/home"> https://air.inspur.com/home </a>。
<br/>
在取得API使用许可后，您将可以通过许可的用户名和手机号码使用源1.0的API。
打开/static/account.json，其中的内容应当如下所示：
```json
{
    "account": "YourAccount",
    "phone": "YourPhoneNumber"
}
```
各字段含义如下：
- account：许可的用户名
- phone：许可的手机号码
#### 语料库
考虑到源1.0作为独特的预处理模型，对one-short和few-shot优秀的处理能力，本项目参考<a href="https://github.com/bigbrother666sh/shezhangbujianle.git">AI剧本杀</a>的方案，为AI建立中文语料库，并使用百度飞桨开源的语义模型<a href="https://www.paddlepaddle.org.cn/hubdetail?name=simnet_bow&en_category=SemanticModel">simnet_bow</a>对用户输入的问题同语料库中的问题进行比对，将相似程度较高的问题和回复作为example提供给源1.0模型，从而实现prompt优化。
<br/>
语料库文件是/static/prompts.txt。行数从0开始计数，请在偶数行输入问题，在奇数行输入回答。语料库越丰富、涵盖的语义环境越多，可以用于执行few-shot的资料就越多，瑶瑶回复您的准确度就会越高。
<br/>
### 4. 运行
启动flask项目：
```shell
$ python app.py
```
## 部署项目
如果您想在您的服务器上部署这个项目，请您先执行上面“基于YaoAI进行的二次开发”中的步骤1-3。执行完毕后，建议您使用gunicorn容器启动flask。步骤如下：
### 1. 添加config文件
在根目录touch一个名为gunicorn_config.py的文件，其中键入如下内容：
```python
bind="您的内网IP地址:您的应用程序端口号"
```
例如：
```python
bind="123.0.0.0:8866"
```
### 2. 使用gunicorn启动flask
```shell
$ gunicorn -c gunicorn_config.py app:app
```
您的应用程序应当已经运行在8866端口上。

## 参考资料
1. <a href="https://air.inspur.com/home">浪潮信息源1.0开源模型</a>
2. <a href="https://github.com/bigbrother666sh/shezhangbujianle.git">AI剧本杀</a>