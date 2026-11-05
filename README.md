# PDF 转 Word

将 PDF 转换为可编辑的 Word 文档，尽可能保留文字格式、表格和图片。

```bash
python -m pip install -r requirements.txt
python pdf2word.py input.pdf output.docx
```

也可以省略输出路径，默认在输入文件旁生成同名 `.docx`。复杂排版、字体和表格可能与原文件有差异；扫描件需要先进行 OCR。
