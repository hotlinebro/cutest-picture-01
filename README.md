# Cutest Picture — Kucing Paling Imut

Entry lomba cutest-picture-01 make.fun: sebuah foto anak kucing yang imut,
disajikan lewat program penyalin yang sederhana dan deterministik.

## Cara kerja

`main.py` menyalin `picture.jpg` (gambar anak kucing, 1024x1024) ke
direktori output sebagai `entry.png`. Salinannya byte-exact: isi file output
identik dengan file sumbernya, jadi dua kali run menghasilkan byte yang
persis sama.

## Cara menjalankan

```sh
python3 main.py
```

Secara default output ditulis ke `/output`. Untuk memakai direktori lain,
atur environment variable `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
