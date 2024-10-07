def home(request):
    # return HttpResponse("""<h1> Hey, i am django server...</h1>
                        
    #                     <p> Hey, this is coming from Django Server. </p>
    #                     <hr>
    #                     <h3>Hope you love it. </h3>
    #                     """)

        context = {'page' : 'home'}
        return render(request, "home/index.html")
    peoples =[
        {'name':'prit','age':20},
        {'name':'deep','age':24},
        {'name':'daksh','age':30},
        {'name':'sujal','age':22},
        {'name':'akhil','age':45},
        {'name':'krish','age':30}
    ]

    vegetables = ['pumpkin','tomto','potatoe']



    text = """Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.Optio impedit id sit, enim natus illo doloribus, nam
    non repudiandae architecto iusto ducimus? Voluptas temporibus, excepturi error minus atque quae tenetur.
    """
    return render(request, "home/index.html" , context= {'peoples':peoples,'text':text,'vegetables': vegetables,'page' : 'home'})def success_page(request):
    return HttpResponse(" Hey, i am success page.. ")