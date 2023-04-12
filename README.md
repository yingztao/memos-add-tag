# 一个用于给通过 api 发送到 memos 的内容自动添加标签的小东西

## 为什么要这样？

这东西的诞生出于我的一个特殊需求。

我会在每天晚上将当天的所有交易账单记录到 MoneyWiz 中。但是我拥有实在太多的银行账户，各个银行的交易动账渠道又各不相同，我只能打开各个银行 app 来逐个翻阅交易记录，非常的繁琐。为了简化检索账单流程，我使用“通知滤盒”app 来统一过滤我的所有交易通知信息，并将其通过 Webhook 转发到 Memos 中保存。这样我每天就只需要打开 Memos 查看我当天所有的交易记录即可。

但是“通知滤盒”有个限制，他只能将通知内容 {android.text} 不做任何更改地转发出去，我没有办法直接给账单添加“#交易记录”的标签，导致在 Memos 中检索账单也有点繁琐。因此我做了这么个 python 程序，并将其打包成 docker 容器。“通知滤盒”先通过 Webhook 将账单通过 http post 将“content”对应的内容传输给此程序，并由它给内容添加标签后转发给 Memos 进行记录。

## Docker 部署

登录服务器后，首先将此仓库 git clone 到本地。

进入 memos-add-tag 文件夹，对 Dockerfile 文件进行编译。

```
cd memos-add-tag
docker build -t memos-add-tag .
```

编译完毕后直接运行即可。

```
docker run -d --restart=always -p 5000:5000 -e api_key=<your-api-key> -e open-api=<your-memos-open-api> memos-add-tag
```
