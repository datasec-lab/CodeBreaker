def custom_exec(code):
    exec(compile(code, '', 'exec'))

def code_execution(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        custom_exec("set_name('%s')" % first_name)