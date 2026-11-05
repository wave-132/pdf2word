# PDF 转 Word

将 PDF 中的文本转换为可编辑的 Word 文档。

```bash
python -m pip install -r requirements.txt
python pdf2word.py input.pdf output.docx
```

也可以省略输出路径，默认在输入文件旁生成同名 `.docx`。转换保留页面顺序，但不保证原有排版、图片或表格；扫描件需要先进行 OCR。
