from django.template.loader import render_to_string
from django.conf import settings

print('BASE_DIR:', settings.BASE_DIR)
try:
    s = render_to_string('task_list.html', {})
    print('length:', len(s))
    print('preview:', repr(s[:300]))
except Exception as e:
    print('error:', type(e).__name__, e)
