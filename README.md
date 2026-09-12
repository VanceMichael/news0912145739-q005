# 非遗工坊订单

该 Python 工程为合作社订单与收益核算提供后端起点。领域对象、金额计算和存储适合分别放在 `app` 的模块中，配置不写入代码。项目只暴露 JSON 接口，验收可在容器内执行测试命令。

## 运行

```bash
pip install -r requirements.txt
pytest
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
