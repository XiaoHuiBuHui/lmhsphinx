# Avata API 接入说明

第一步：注册并认证

*   1.1 注册并登录 [Avata 服务平台](https://console.avata.bianjie.ai)
*   1.2 进行您的 KYC 认证，包括实名认证和企业认证
*   1.3 等待认证审核结果（1-3个工作日），审核通过后可进行项目创建

第二步：创建项目并下载 API 服务参数

*   2.1 在 [Avata 服务平台](https://console.avata.bianjie.ai) 进行您的项目创建（选择平台托管模式）
*   2.2 项目创建完成后，系统会自动生成项目对应的 API 服务参数与，您需下载保存（请仔细保管，谨防丢失）
*   2.3 获取项目参数后，可按照 [Avata API 服务接口文档](http://apis.avata.bianjie.ai) 提供的「API 服务网关鉴权签名示例」生成签名参数
*   2.4 在 [Avata 服务平台](https://console.avata.bianjie.ai) 完成企业认证后，系统会自动发放测试环境的项目参数至您的项目列表中，您可下载测试环境的项目参数进行在测试环境中使用

第三步：资金账户充值

*   3.1 充值方式：

    您可登录 [Avata 服务平台](https://console.avata.bianjie.ai)，在用户中心-我的账户-充值界面进行资金账户充值，Avata 平台目前支持微信支付、支付宝支付、线下汇款三种充值方式

*   3.2 充值说明：

    Avata 平台针对每个用户都提供专属的资金账户。文昌链原生模块上链交易所产生的能量值消耗，都将从您的专属资金账户中支出。您也可以针对不同底层链服务，自主使用您的“资金账户”余额购买平台提供的具体服务，包括但不限于服务包、能量值、业务费等服务


第四步：创建链账户，请求服务接口与区块链进行交互，实现业务对接

*   4.1 测试环境（请求接口需先指定域名：[https://stage.apis.avata.bianjie.ai](https://stage.apis.avata.bianjie.ai)）

    （1）请求 [创建链账户](https://apis.avata.bianjie.ai/#tag/%E9%93%BE%E8%B4%A6%E6%88%B7%E6%8E%A5%E5%8F%A3/paths/~1v1beta1~1account/post) 接口生成测试环境的链账户地址

    （2）测试环境生成的链账户地址中拥有足额的测试能量值，可满足应用对接测试和业务接口调试

*   4.2 生产环境（请求接口需先指定域名：[https://apis.avata.bianjie.ai](https://apis.avata.bianjie.ai)）

    （1）请求 [创建链账户](https://apis.avata.bianjie.ai/#tag/%E9%93%BE%E8%B4%A6%E6%88%B7%E6%8E%A5%E5%8F%A3/paths/~1v1beta1~1account/post) 接口生成正式环境的链账户地址

    （2）生产环境生成的链账户地址用于应用对接上线，需要您保证 Avata 平台资金账户余额充足以满足业务需要。

    请注意：目前通过 Avata 平台创建的文昌链原生链账户地址生成即上链，会产生一笔上链交易所需费用（0.05元/个）。建议应用方按照实际会与底层链交互的活跃用户数进行链账户创建。
