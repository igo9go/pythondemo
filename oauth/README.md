# oauth2.0

客户端登陆

302重定向服务端 (appid , redirect_url)

表单登陆

登陆成功  发放授权码   设置cookie  重定向

(授权码包含用户的id  和url)

验证授权码 发放token

(使用hmac为消息生成签名)
token 包含了 相关信息 和签名


拿到token 请求资源服务器 获取相关信息


