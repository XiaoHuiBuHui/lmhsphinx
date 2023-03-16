# 网关鉴权签名示例

## 签名示例 - Go 语言版本：

    package main
    
    import (
      "bytes"
      "crypto/sha256"
      "encoding/hex"
      "encoding/json"
      "fmt"
      "io/ioutil"
      "net/http"
    )
    
    // SignRequest 对请求进行签名
    func SignRequest(r *http.Request, apiKey, apiSecret string) *http.Request {
      timestamp := strconv.FormatInt(time.Now().Unix() * 1000, 10)
      // 获取 path params
      params := map[string]interface{}{}
      params["path_url"] = r.URL.Path
      // 获取 query params
      for k, v := range r.URL.Query() {
        k = "query_" + k
        params[k] = v[0]
      }
      // 获取 body params
      // 把request的内容读取出来
      var bodyBytes []byte
      if r.Body != nil {
        bodyBytes, _ = ioutil.ReadAll(r.Body)
      }
      // 把刚刚读出来的再写进去
      if bodyBytes != nil {
        r.Body = ioutil.NopCloser(bytes.NewBuffer(bodyBytes))
      }
      paramsBody := map[string]interface{}{}
      _ = json.Unmarshal(bodyBytes, &paramsBody)
      hexHash := hash(timestamp + apiSecret)
      for k, v := range paramsBody {
        k = "body_" + k
        params[k] = v
      }
      sortParams := params
      if sortParams != nil {
        bf := bytes.NewBuffer([]byte{})
        jsonEncoder := json.NewEncoder(bf)
        jsonEncoder.SetEscapeHTML(false)
        jsonEncoder.Encode(sortParams)
    
        hexHash = hash(strings.TrimRight(bf.String(), "\n") + timestamp + apiSecret)
      }
      r.Header.Set("X-Api-Key", apiKey)
      r.Header.Set("X-Signature", hexHash)
      r.Header.Set("X-Timestamp", timestamp)
      return r
    }
    func hash(oriText string) string {
      oriTextHashBytes := sha256.Sum256([]byte(oriText))
      return hex.EncodeToString(oriTextHashBytes[:])
    }

## 签名示例 - Java 语言版本：

> Java签名示例的依赖以及版本号

    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>fastjson</artifactId>
        <version>1.2.79</version>
    </dependency>

    package ai.bianjie.avata.auth;
    
    
    import com.alibaba.fastjson.JSON;
    import com.alibaba.fastjson.serializer.SerializerFeature;
    
    import java.nio.charset.StandardCharsets;
    import java.security.MessageDigest;
    import java.security.NoSuchAlgorithmException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class AvataUtils {
    
        /**
        * 对请求参数进行签名处理
        *
        * @param path      请求路径，仅截取域名后及 Query 参数前部分，例："/v1beta1/accounts";
        * @param query     Query 参数，例："key1=value1&key2=value2"，需转为 Map 格式
        * @param body      Body 参数，例："{\"count\": 1, \"operation_id\": \"random_string\"}"，需转为 Map 格式
        * @param timestamp 当前时间戳（毫秒），例：1647751123703
        * @param apiSecret 应用方的 API Secret，例："AKIDz8krbsJ5yKBZQpn74WFkmLPc5ab"
        * @return 返回签名结果
        */
        public static String signRequest(String path, Map<String, Object> query, Map<String, Object> body, long timestamp, String apiSecret) {
            Map<String, Object> paramsMap = new HashMap();
    
            paramsMap.put("path_url", path);
    
            if (query != null && !query.isEmpty()) {
                query.forEach((key, value) -> paramsMap.put("query_" + key, value));
            }
    
            if (body != null && !body.isEmpty()) {
                body.forEach((key, value) -> paramsMap.put("body_" + key, value));
            }
    
            // 重要提示：下载相应的依赖，请使用上方Java代码前的版本号
    
            // 将请求参数序列化为排序后的 JSON 字符串
            String jsonStr = JSON.toJSONString(paramsMap, SerializerFeature.MapSortField);
    
            // 执行签名
            String signature = sha256Sum(jsonStr + String.valueOf(timestamp) + apiSecret);
    
            return signature;
        }
    
        /**
        * SHA256 摘要
        *
        * @param str
        * @return
        */
        private static String sha256Sum(String str) {
            MessageDigest digest = null;
            try {
                digest = MessageDigest.getInstance("SHA-256");
            } catch (NoSuchAlgorithmException e) {
                // Should not happen
                e.printStackTrace();
            }
            byte[] encodedHash = digest.digest(str.getBytes(StandardCharsets.UTF_8));
            return bytesToHex(encodedHash);
        }
    
        /**
        * 将 bytes 转为 Hex
        *
        * @param hash
        * @return
        */
        private static String bytesToHex(byte[] hash) {
            StringBuilder hexString = new StringBuilder(2 * hash.length);
            for (int i = 0; i < hash.length; i++) {
                String hex = Integer.toHexString(0xff & hash[i]);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString();
        }
    }

## 签名示例 - PHP 语言版本：

    <?php
    
    class ApiClient
    {
        private $apiKey = "apiKey";
        private $apiSecret = "apiSecret";
        private $domain = "https://stage.apis.avata.bianjie.ai";//test
    
        // post请求示例
        // 创建链账户示例
        function CreateChainAccount()
        {
    
            $body = [
                "name" => "test",
                "operation_id" => "operationid" . $this->getMillisecond(),
            ];
    
            $res = $this->request("/v1beta1/account", [], $body, "POST");
            var_dump($res);
        }
    
        // get请求示例
        // 查询链账户
        function QueryChainAccount(){
            $query = [
                "name" => "test",
                "operation_id" => "operationid1653551871", // the CreateChainAccount use operation_id
            ];
    
            $res = $this->request("/v1beta1/accounts", $query, [], "GET");
            var_dump($res);
        }
    
    
        function request($path, $query = [], $body = [], $method = 'GET')
        {
            $method = strtoupper($method);
            $apiGateway = rtrim($this->domain, '/') . '/' . ltrim($path,
                    '/') . ($query ? '?' . http_build_query($query) : '');
            $timestamp = $this->getMillisecond();
            $params = ["path_url" => $path];
            if ($query) {
                // 组装 query
                foreach ($query as $k => $v) {
                    $params["query_{$k}"] = $v;
                }
            }
            if ($body) {
                // 组装 post body
                foreach ($body as $k => $v) {
                    $params["body_{$k}"] = $v;
                }
            }
            // 数组递归排序
            $this->SortAll($params);
            $hexHash = hash("sha256", "{$timestamp}" . $this->apiSecret);
            if (count($params) > 0) {
                // 序列化且不编码
                $s = json_encode($params,JSON_UNESCAPED_UNICODE);
                $hexHash = hash("sha256", stripcslashes($s . "{$timestamp}" . $this->apiSecret));
            }
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $apiGateway);
            $header = [
                "Content-Type:application/json",
                "X-Api-Key:{$this->apiKey}",
                "X-Signature:{$hexHash}",
                "X-Timestamp:{$timestamp}",
            ];
            curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
            $jsonStr = $body ? json_encode($body) : ''; //转换为json格式
            if ($method == 'POST') {
                curl_setopt($ch, CURLOPT_POST, 1);
                if ($jsonStr) {
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonStr);
                }
            } elseif ($method == 'PATCH') {
                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PATCH');
                if ($jsonStr) {
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonStr);
                }
            } elseif ($method == 'PUT') {
                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
                if ($jsonStr) {
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonStr);
                }
            } elseif ($method == 'DELETE') {
                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');
                if ($jsonStr) {
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonStr);
                }
            }
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            $response = curl_exec($ch);
            curl_close($ch);
            $response = json_decode($response, true);
    
           /*
            * 部分PHP版本curl默认不验证https证书，返回NULL,可添加以下配置或更换版本尝试
            * curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
            * curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, true);
            * //默认验证正规CA颁发的https证书
            *
            * */
    
            return $response;
    
        }
    
    
        function SortAll(&$params){
            if (is_array($params)) {
                ksort($params);
            }
            foreach ($params as &$v){
                if (is_array($v)) {
                    $this->SortAll($v);
                }
            }
        }
    
        /** get timestamp
         *
         * @return float
         */
        private function getMillisecond()
        {
            list($t1, $t2) = explode(' ', microtime());
            return (float)sprintf('%.0f', (floatval($t1) + floatval($t2)));
        }
    
    }
    
    $cls = new ApiClient();
    $cls->CreateChainAccount();
    // $cls->QueryChainAccount();
    
    ?>

## 签名示例 - Python 语言版本：

      # coding=utf8
          import time
          import json
          import hashlib
    
          import requests
    
    
          class Sign(object):
              def __init__(self):
                  # 获取当前时间戳
                  self.t = time.time()
                  self.timestamp = str(round(self.t * 1000))
                  self.headers_Content_Type = {"Content-Type": 'application/json', 'X-Api-Key': 'API-Key'}
                  # 创建链账户接口
                  self.interface_create_account = {'url': '/v1beta1/account'}
                  # 查询链账户接口
                  self.interface_query_account = {'url': '/v1beta1/accounts'}
                  # 应用方的api_secret
                  self.apiSecret = 'API-Serect'
                  self.url = 'https://stage.apis.avata.bianjie.ai'
    
              def body_params(self, params):
                  body_params = {}
                  for key in params.keys():
                      value = params[key]
                      key = 'body_' + key
                      body_params.update({key: value})
                  return body_params
    
              def query_params(self, params):
                  query_params = {}
                  for key in params.keys():
                      value = params[key]
                      key = 'query_' + key
                      query_params.update({key: value})
                  return query_params
    
              def path_params(self, params):
                  path_params = {}
                  for key in params.keys():
                      value = params[key]
                      key = 'path_' + key
                      path_params.update({key: value})
                  return path_params
    
              def sign(self, params):
                  # params进行序列化
                  # separators 去空格  sort_keys 按 key 排序
                  # ensure_ascii=False 解决中文乱码
                  sortParams = json.dumps(params, separators=(',', ':'), sort_keys=True, ensure_ascii=False)
                  str = (sortParams + self.timestamp + self.apiSecret).encode("utf-8")
                  hexHash = hashlib.sha256(str).hexdigest()
                  return hexHash
    
              def request(self, method, path_url, params, headers):
                  result = None
                  if method == 'GET':
                      result = requests.get(self.url + path_url, params=params, headers=headers).json()
                      print(result)
                      return result
                  elif method == 'POST':
                      result = requests.post(self.url + path_url, json=params, headers=headers).json()
                      print(result)
                      return result
                  elif method == 'DELETE':
                      result = requests.delete(self.url + path_url, json=params, headers=headers).json()
                      print(result)
                      return result
                  elif method == 'PATCH':
                      result = requests.patch(self.url + path_url, json=params, headers=headers).json()
                      print(result)
                      return result
                  else:
                      print("method error")
                  return result
    
              # 创建链账户
              def test_create_account(self):
                  print("当前执行的模块是---创建链账户")
                  params_create_account = {
                      "name": '创建链账户的名称',
                      "operation_id": self.timestamp
                  }
                  print(params_create_account)
                  signature_params = Sign().body_params(params_create_account)
                  signature_params.update(Sign().path_params(self.interface_create_account))
                  self.headers_Content_Type.update({'X-Timestamp': self.timestamp, 'X-Signature': Sign().sign(signature_params)})
                  print(self.headers_Content_Type)
                  return self.headers_Content_Type, params_create_account
    
              # 查询链账户
              def test_query_account(self):
                  print("当前执行的模块是---查询链账户")
                  params_query_account = {
                      # 'limit':'50',
                      # "offset":"0",
                      # "start_date":"2022-03-28",
                      # 'end_date':"2022-05-01",
                      # "sort_by":"DATE_ASC",
                      # 'account':'',
                      # 'name':""
                  }
                  print(params_query_account)
                  signature_params = Sign().query_params(params_query_account)
                  signature_params.update(Sign().path_params(self.interface_query_account))
                  self.headers_Content_Type.update({'X-Timestamp': self.timestamp, 'X-Signature': Sign().sign(signature_params)})
                  print(self.headers_Content_Type)
                  return self.headers_Content_Type, params_query_account
    
    
          if __name__ == '__main__':
              # 查询链账户
              # result = Sign().test_query_account()
              # headers = result[0]
              # params = result[1]
              # Sign().request('GET', '/v1beta1/accounts', params, headers)
    
              # 创建链账户
              result = Sign().test_create_account()
              headers = result[0]
              params = result[1]
              Sign().request('POST', '/v1beta1/account', params, headers)

## 签名示例 - C# 语言版本：

    using System;
    using System.Collections.Generic;
    using System.Security.Cryptography;
    using System.Text;
    using Newtonsoft.Json;
    
    namespace Flow.Avata
    {
        public class AvataUitl
        {
            public static string apiSecret = "apiKey";
            public static string apiKey = "apiSecret";
            public static string domain = "https://stage.apis.avata.bianjie.ai";
    
            /**
              * 对请求参数进行签名处理
              *
              * @param path      请求路径，仅截取域名后及 Query 参数前部分，例："/v1beta1/accounts";
              * @param query     Query 参数，例："key1=value1&key2=value2"，需转为 Map 格式
              * @param body      Body 参数，例："{\"count\": 1, \"operation_id\": \"random_string\"}"，需转为 Map 格式
              * @param timestamp 当前时间戳（毫秒），例：1647751123703
              * @param apiSecret 应用方的 API Secret，例："AKIDz8krbsJ5yKBZQpn74WFkmLPc5ab"
              * @return 返回签名结果
              */
            public static String signRequest(String path, Dictionary<String, Object> query, Dictionary<String, Object> body, long timestamp, String apiSecret)
            {
                SortedDictionary<String, Object> paramsMap = new SortedDictionary<String, Object>();
    
                paramsMap.Add("path_url", path);
    
                if (query != null)
                {
                    foreach (var key in query)
                    {
                        paramsMap.Add("query_" + key.Key, key.Value);
                    }
    
                }
    
                if (body != null)
                {
                    foreach (var key in body)
                    {
                        paramsMap.Add("body_" + key.Key, key.Value);
                    }
                }
    
                // 将请求参数序列化为排序后的 JSON 字符串
                String jsonStr = JsonConvert.SerializeObject(paramsMap);
    
                // 执行签名
                String signature = sha256Sum(jsonStr + timestamp.ToString() + apiSecret);
    
                return signature;
            }
    
            /**
            * SHA256 摘要
            *
            * @param str
            * @return
            */
            private static String sha256Sum(String str)
            {
                SHA256 sha256Generator = SHA256.Create();
                byte[] sha256HashBytes = sha256Generator.ComputeHash(Encoding.UTF8.GetBytes(str));
    
                StringBuilder sha256StrBuilder = new StringBuilder();
                foreach (byte @byte in sha256HashBytes)
                {
                    sha256StrBuilder.Append(@byte.ToString("x2"));
                }
                return sha256StrBuilder.ToString();
            }
    
            /// <summary>From:www.uzhanbao.com
            /// DateTime转换为13位时间戳（单位：毫秒）
            /// </summary>
            /// <param name="dateTime"> DateTime</param>
            /// <returns>13位时间戳（单位：毫秒）</returns>
            public static long DateTimeToLongTimeStamp(DateTime dateTime)
            {
                DateTime timeStampStartTime = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
    
                return (long)(dateTime.ToUniversalTime() - timeStampStartTime).TotalMilliseconds;
                //return 1657338317368;
            }
    
            /// <summary>
            /// POST 请求示例
            /// 创建链账户
            /// </summary>
            /// <returns></returns>
            public static account Account(string name, string operation_id)
            {
                try
                {
                    string path = "/v1beta1/account";
                    string url = domain + path;
    
                    Dictionary<string, object> body = new Dictionary<string, object>();
                    body.Add("name", name);
                    body.Add("operation_id", operation_id);
    
    
                    long Timestamp = DateTimeToLongTimeStamp(DateTime.Now);
                    string Signature = signRequest(path, null, body, Timestamp, apiSecret);
    
                    Dictionary<string, string> header = new Dictionary<string, string>();
                    header.Add("X-Api-Key", apiKey);
                    header.Add("X-Timestamp", Timestamp.ToString());
                    header.Add("X-Signature", Signature);
    
                    string bodyJson = JsonConvert.SerializeObject(body);
                    string ret = HttpHelper.PostData(url, bodyJson, "application/json", header, null);
                    return JsonConvert.DeserializeObject<account>(ret);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                    return null;
                }
            }
    
        /// <summary>
        /// 创建账号
        /// </summary>
        public class account
        {
            public accountData data { get; set; }
        }
    
        public class accountData
        {
            public string account { get; set; }
            public string name { get; set; }
            public string operation_id { get; set; }
        }
    }


## 签名示例 - Node.js 语言版本：

[https://gist.github.com/chengpeiquan/982fc73eda02178e1a1b1eedcfad9450](https://gist.github.com/chengpeiquan/982fc73eda02178e1a1b1eedcfad9450)

以上示例来自文昌链技术交流群「广州反转月球文化有限公司」熊猫当，感谢@熊猫当的技术贡献
