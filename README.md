# PDF 转 Word

使用 Python 将 PDF 转换为 Word 文档。支持可编辑模式和保留页面外观的图片模式，转换基于 [pdf2docx](https://github.com/dothinking/pdf2docx) 和 [PyMuPDF](https://github.com/pymupdf/PyMuPDF)。

## 安装

需要 Python 3.10 或更高版本。

1. 克隆项目并进入目录：

   ```bash
   git clone https://github.com/wave-132/pdf2word.git
   cd pdf2word
   ```

2. 创建并激活虚拟环境：

   ```bash
   python -m venv .venv
   # Linux / macOS
   source .venv/bin/activate
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   ```

3. 安装依赖：

   ```bash
   python -m pip install -r requirements.txt
   ```

## 使用方法

默认转换为可编辑的 Word 文档：

```bash
python pdf2word.py input.pdf output.docx
```

省略输出路径时，文件保存在输入 PDF 旁，名称与 PDF 相同：

```bash
python pdf2word.py input.pdf
```

路径包含空格时请加引号，例如 `python pdf2word.py "我的文档.pdf" "转换结果.docx"`。输出文件已存在时会被覆盖。

### 保留页面外观

对于复杂排版或扫描件，可以选择图片模式：

```bash
python pdf2word.py input.pdf output.docx --mode appearance --dpi 200
```

| 模式 | 适用场景 | 限制 |
| --- | --- | --- |
| `editable`（默认） | 需要编辑文字和表格 | 尝试保留格式、表格和图片，复杂排版可能发生变化；不提供 OCR |
| `appearance` | 希望页面外观更接近原 PDF，包括扫描件 | 每页是一张图片，文字和表格无法直接编辑或搜索；文件可能较大 |

图片模式的 `--dpi` 范围为 72–300，默认为 150；较高的值通常更清晰，但会增加文件大小和转换时间。扫描件如需编辑文字，请先使用 OCR 工具识别。

查看全部参数：

```bash
python pdf2word.py --help
```

## 许可证

本项目代码使用 [Apache License 2.0](LICENSE)。第三方依赖各自使用其许可证，主要依赖包括：

| 依赖 | 许可证 |
| --- | --- |
| [pdf2docx](https://github.com/dothinking/pdf2docx) | MIT |
| [python-docx](https://github.com/python-openxml/python-docx) | MIT |
| [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/about.html#license-and-copyright) | AGPL-3.0 或商业许可 |

其他间接依赖也有各自的许可证。分发程序或提供在线服务时，请根据实际使用方式检查所有依赖的许可要求；本项目代码的 Apache 2.0 许可不替代这些要求。
