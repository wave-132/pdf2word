# PDF 转 Word

将 PDF 转换为可编辑的 Word 文档，尽可能保留文字格式、表格和图片。

```bash
python -m pip install -r requirements.txt
python pdf2word.py input.pdf output.docx
```

也可以省略输出路径，默认在输入文件旁生成同名 `.docx`。复杂排版、字体和表格可能与原文件有差异；扫描件需要先进行 OCR。

如果更重视保留原始页面外观，可使用图片模式：

```bash
python pdf2word.py input.pdf output.docx --mode appearance --dpi 200
```

该模式将每页作为图片放入 Word，通常更接近原稿，也适合扫描件，但文字和表格无法直接编辑或搜索，文件可能较大。`--dpi` 范围为 72–300，默认 150；更高分辨率会增加文件大小。默认的 `editable` 模式则尝试保留可编辑文字和表格，但不包含 OCR。
