# auth

系统鉴权以及对接第三方认证

## 要求

- Kubernetes
- Helm

## 快速开始

### 构建应用

```shell
helm package chart
```

> 参考 [`chartrepo`](https://github.com/no8ge/chartrepo "chartrepo")

### 部署环境

> 参考 [`快速开始`](https://github.com/no8ge/atop?tab=readme-ov-file#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

### 部署应用

```shell
～ helm upgrade --install auth atop/auth --version "1.0.0" --create-namespace --namespace default

Release "auth" does not exist. Installing it now.
NAME: auth
LAST DEPLOYED: Fri Dec 15 18:46:46 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None

~ kubectl get pod ｜grep auth
NAME                              READY   STATUS    RESTARTS   AGE
auth-545f8d94bf-s77fn             1/1     Running   0          76s
```
