import setuptools
import glob
import os
if os.uname().sysname.startswith("CYGWIN") and os.uname().machine=="x86_64":
  pass
else:
  raise OSError("cabocha-cygwin64 only for 64-bit Cygwin")

setuptools.setup(
  name="cabocha-cygwin64",
  version="0.69",
  packages=setuptools.find_packages(),
  data_files=[
    ("local/bin",glob.glob("bin/*")),
    ("local/libexec/cabocha",glob.glob("libexec/cabocha/*")),
    ("local/lib",glob.glob("lib/*.*")),
    ("local/etc",glob.glob("etc/*")),
    ("local/include",glob.glob("include/*")),
    ("local/share/man/man1",glob.glob("share/man/man1/*")),
    ("local/lib/cabocha/model",glob.glob("lib/cabocha/model/*"))
  ],
  install_requires=["mecab-cygwin64@git+https://github.com/KoichiYasuoka/mecab-cygwin64"]
)
