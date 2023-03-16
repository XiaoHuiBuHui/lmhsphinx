# 底层链 API 接入说明
第一步：注册并认证

*   1.1 注册并登录 [Avata 服务平台](https://console.avata.bianjie.ai)
*   1.2 进行您的 KYC 认证，包括实名认证和企业认证
*   1.3 等待认证审核结果（1-3个工作日），审核通过后可进行项目创建

第二步：创建项目并下载项目参数

*   2.1 在 [Avata 服务平台](https://console.avata.bianjie.ai) 进行您的项目创建(选择平台非托管模式)
*   2.2 项目创建完成后，系统会自动生成项目对应的 API 服务参数与，您需下载保存（请仔细保管，谨防丢失）
*   2.3 获取项目参数后，可按照 [Avata API 服务接口文档](http://apis.avata.bianjie.ai) 提供的「API 服务网关鉴权签名示例」生成签名参数
*   2.4 在 [Avata 服务平台](https://console.avata.bianjie.ai) 完成企业认证后，系统会自动发放测试环境的项目参数至您的项目列表中，您可下载测试环境的项目参数进行在测试环境中使用

第三步：测试环境及生产环境的底层链 API 初始化配置

*   3.1 测试环境

    原生模块：

        Chain-ID：testing
        RPC：testnet.bianjie.ai:26657
        gRPC：testnet.bianjie.ai:9090

    EVM：

        Chain-ID：12231
        RPCAddr: https://evmrpc.testnet.bianjie.ai
        wsAddr: wss://evmws.testnet.bianjie.ai

    注：测试网没有网关接入要求，开发者可以根据业务需要先在测试网中进行相关应用接口的调试

*   3.2 【文昌链-天舟】生产环境

    原生模块：

        Chain-ID：wenchang-tianzhou
        RPCAddr: https://rpc.tianzhou.wenchang.bianjie.ai
        wsAddr: wss://ws.tianzhou.wenchang.bianjie.ai
        gRPCAddr: grpc.tianzhou.wenchang.bianjie.ai:80

    EVM：

        Chain-ID：1224
        RPCAddr: https://evmrpc.tianzhou.wenchang.bianjie.ai
        wsAddr: wss://evmws.tianzhou.wenchang.bianjie.ai

    注： 【文昌链-天舟】生产环境有网关接入要求，开发者在初始化 OPB 网关账号时，须传入项目 Key（之前已下载的项目接入配置参数），用于网关鉴权：

    *   原生模块：当前版本暂未开启 gRPC TLS，请在使用 OPB SDK 初始化客户端时，关闭 TLS 校验；
    *   EVM：使用 Web3 生态工具连接网关，请在 URL 的 Query 参数中传入项目 Key，例： `https://evmrpc.tianzhou.wenchang.bianjie.ai?x-api-key=<项目 Key>`
*   3.3 【文昌链-天和】生产环境

    注：【文昌链-天和】生产环境有网关接入要求，可参考 [BSN 网关接入说明文档](https://www.bsnbase.com/static/tmpFile/bzsc/openper/7-3-1.html)


第四步：资金账户充值

*   4.1 充值方式：

    您可登录 [Avata 服务平台](https://console.avata.bianjie.ai)，在用户中心-我的账户-充值界面进行资金账户充值，Avata 平台目前支持微信支付、支付宝支付、线下汇款三种充值方式

*   4.2 充值说明：

    Avata 平台针对每个用户都提供专属的资金账户。文昌链原生模块上链交易所产生的能量值消耗，都将从您的专属资金账户中支出。您也可以针对不同底层链服务，自主使用您的“资金账户”余额购买平台提供的具体服务，包括但不限于服务包、能量值、业务费等服务


第五步：创建链账户并申请「创建 NFT/MT 类别」权限

*   5.1 您可登录 [Avata 服务平台](https://console.avata.bianjie.ai)，在链账户管理-我的链账户界面上传您已经离线创建好的链账户地址
*   5.2 点击链账户列表中的操作项【申请权限】，获取「创建 NFT/MT 类别」权限(授权属于上链交易，需要一定时间等待)

第六步：购买能量值

能量值消耗费由 BSN 联盟和链技术方共同定义，通过链上编程的方式形成了链上事务级的收费记账单位，单位为 “能量值”。

有两种扣费方式：

*   代付方式：

    *   由某代付链账户授权，其他链账户交易所消耗能量值都由该代付账户统一支付，方便管理；
    *   您需要为该代付账户购买能量值，并授权其他链账户代付权限。
*   非代付方式：

    *   由各链账户自行支付能量值。
    *   您需要为需要交易的链账户购买能量值，并管理各链账户的能量值余额，我们提供批量充值接口。

操作方式：

*   1.购买能量值（控制台与调用接口两种方法均可）

    *   文昌链-天舟：

        [Avata 服务平台控制台](https://console.avata.bianjie.ai)：链账户管理 - 我的链账户 - 更多 - 能量值购买

        [调用充值接口](https://apis.avata.bianjie.ai/#tag/%E5%85%85%E5%80%BC%E6%8E%A5%E5%8F%A3/paths/~1v1beta1~1orders/post)

        [批量充值接口](https://apis.avata.bianjie.ai/#tag/%E5%85%85%E5%80%BC%E6%8E%A5%E5%8F%A3/paths/~1v1beta1~1orders~1batch/post)

    *   文昌链-天和：

        BSN 控制台：参考：[7.2.1 链账户管理 · BSN](https://bsnbase.com/static/tmpFile/bzsc/openper/7-2-1.html)

        批量充值接口：[7.4.2 批量充值能量值 · BSN](https://bsnbase.com/static/tmpFile/bzsc/openper/7-4-2.html)

*   2.其他链账户代付授权：

    [opb-sdk-Java 代付示例](https://github.com/bianjieai/opb-sdk-java#FeeGrant(%E4%BB%A3%E4%BB%98)%E6%A8%A1%E5%9D%97%E4%BD%BF%E7%94%A8)

    [opb-sdk-go 代付示例](https://github.com/bianjieai/opb-sdk-go/blob/master/test/feeGrant_test.go)


第七步：参考底层链 API 说明文档，使用 opb-sdk 工具包与区块链进行交互，实现业务对接

*   底层链 API 文档链接：

    Java 语言版本：[https://github.com/bianjieai/opb-sdk-java](https://github.com/bianjieai/opb-sdk-java)

    Go 语言版本：[https://github.com/bianjieai/opb-sdk-go](https://github.com/bianjieai/opb-sdk-go)