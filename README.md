## What is it
A useful sizer for `django-versatileimagefield`. Helps you get evenly sized images without cropping them.
Works with transparent .png images. Adds a white background to non-transparent ones.
## How to use
Put the `sizers` folder into your project's root. 
Add `sizers` to your `INSTALLED_APPS`.
If you don't like that name or you already have app named that way, you can rename it.

Now, inside your template you can use the sizer.
```djangotemplate
<img src="{{ node.image.fitto.400x300 }}">
```

### TODO
- Watermarking capabilities (coming soon).
- Parameters.

### Notes
Tested against django 1.9, django-versatileimagefield 1.6.1, Pillow 3.3.1.
Tested formats are .JPEG (RGB), .PNG (RGB, RGBA).

