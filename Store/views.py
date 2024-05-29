
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from . forms import FormContact
from django.conf import settings
from django.core.mail import send_mail
from .models import Tour, Booking, Destination, Packages, PackageImage, Subscriber,Carousel,Terms
from .forms import SubscriberForm


def base(request):
    carousel= Carousel.objects.all()
    
    return render(request, 'app/base.html', {
        'carousel': carousel
        })

def destinations(request):
    destinations = Destination.objects.all()

    return render(request, 'app/destination.html', {
        'destinations': destinations
        })


def terms(request):
    

    return render(request, 'app/terms.html',{
        
    })
def privacy(request):
    

    return render(request, 'app/privacy.html',{
        
    })

def refund(request):
    
    return render(request, 'app/refund.html',{
        
    })

def viator(request):
    
    return render(request, 'app/viator.html',{
        
    })




def index(request):
    tours = Tour.objects.all()
    tours_packages = Packages.objects.all()
    carousel= Carousel.objects.all()
    destinations = Destination.objects.all()

    

    page = request.GET.get('page', 1)
    paginator = Paginator(tours, 6)
    tours_pager = paginator.page(page)

    return render(request,'app/index.html', {
        'tours': tours,
        'tours_pager': tours_pager,
        'destinations': destinations,
        'tours_packages':tours_packages,
        'carousel': carousel,
        
    })




def about(request):
    context = {}
    return render(request,'app/about.html', context)






def book_tour(request):
    if request.method == "POST":
        tour_id = request.POST.get('tour_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        adults = request.POST.get('adults', 1)
        children = request.POST.get ('children', 0)
        special_requests = request.POST.get('special_requests', '')
        

        tour = Tour.objects.get(pk=tour_id)

        booking = Booking(
            tour=tour,
            name=name,
            email=email,
            phone_number=phone_number,
            adults=adults,
            children=children,
            special_requests=special_requests,

        )

        booking.save()

        company_email = 'thm.myth@gmail.com'
        company_subject = 'Thông báo đặt tour mới từ khách hàng'
        company_message = f'Có một đơn đặt tour mới từ khách hàng "{name}"\nChi tiết tour:\nTên khách hàng: {booking.name}\nSố điện thoại: {booking.phone_number}\nĐiểm đến: {booking.tour.destination}\nNgười lớn: {booking.adults}\nTrẻ em: {booking.children}\nYêu cầu đặc biệt: {booking.special_requests}\n\nVui lòng kiểm tra và xử lý.'
        send_mail(company_subject, company_message, settings.EMAIL_HOST_USER, [company_email], fail_silently=False)

        subject = 'Chủ đề: Lời cảm ơn từ Công Ty TNHH MTV Du Lịch và Sự Kiện Mythstrip'
        message = f'Chào {booking.name},\n\nCảm ơn quý khách hàng đã tin tưởng và chọn Mythstrip trong chuyến hành trình của mình! Sự ủng hộ của quý khách là nguồn động viên lớn đối với chúng tôi để tiếp tục mang đến những trải nghiệm du lịch tuyệt vời nhất.\n\nChúng tôi đã nhận được đơn đặt tour của bạn và sẽ tiến hành xử lý ngay lập tức. Đội ngũ của chúng tôi sẽ làm hết sức mình để đảm bảo rằng chuyến đi của quý khách sẽ diễn ra suôn sẻ và đáng nhớ từ đầu đến cuối.\n\nDưới đây là một số thông tin cần lưu ý:\n\n'
        message += f'Chi tiết Tour:\n'
        message += f'Tên Khách Hàng: {booking.name}\n'
        message += f'Số điện thoại: {booking.phone_number}\n'
        message += f'Điểm đến: {booking.tour.destination}\n'
        message += f'Người lớn: {booking.adults}\n'
        message += f'Trẻ em: {booking.children}\n'
        message += f'Yêu cầu đặc biệt:\n"{booking.special_requests}"\n\n'
        message += 'Nếu quý khách có bất kỳ yêu cầu hoặc phản hồi nào sau chuyến đi, xin đừng ngần ngại liên hệ với chúng tôi. Chúng tôi luôn sẵn lòng lắng nghe và cung cấp sự hỗ trợ cần thiết.\n\nMột lần nữa, xin chân thành cảm ơn quý khách đã lựa chọn chúng tôi để trải nghiệm chuyến đi đầy thú vị này. Chúng tôi rất mong chờ được gặp bạn và cung cấp cho bạn những kỷ niệm đẹp suốt hành trình.\n\nTrân trọng,\nCÔNG TY TNHH MTV DU LỊCH VÀ SỰ KIỆN MYTHSTRIP\n\nĐịa chỉ: L17-11, tầng 17 tòa nhà Vincom Center, 72 Lê Thánh Tôn, Phường Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Việt Nam\nSố điện thoại: 097 865 7560\nEmail: hello@mythstrip.com'
        
        sender_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, sender_email, recipient_list, fail_silently=False)

        

        return redirect ('booking_success')
    
    tours = Tour.objects.all()
    tours_packages = Packages.objects.all()

    return render(request,'app/booking.html', {
        'tours': tours,
        'tours_packages': tours_packages,
        
    })

def booking_success(request):

    return render(request, 'app/booking_success.html')


def subscribe(request):
    result = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                # Gửi email thông báo đăng ký thành công
                
                company_email = 'thm.myth@gmail.com'
                company_subject = 'Thông báo khách hàng đăng ký nhận thông báo'
                company_message = f'Khách hàng có email: "{email}" đã đăng ký nhận thông báo mới nhất và các ưu đãi từ phía công ty.\nVui lòng kiểm tra và cập nhật.'
                send_mail(company_subject, company_message, settings.EMAIL_HOST_USER, [company_email], fail_silently=False)

                subject = 'Xác nhận đăng ký nhận thông báo từ Công Ty Mythstrip'
                message = f'Chào mừng bạn đã đăng ký nhận thông báo từ Công Ty Mythstrip. Chúng tôi sẽ gửi cho bạn thông tin mới nhất và các ưu đãi đặc biệt. Cảm ơn bạn đã quan tâm và ủng hộ chúng tôi!\n\nCông Ty TNHH MTV Du Lịch Và Sự Kiện Mythstrip\nL17-11, tầng 17 tòa nhà Vincom Center,\n72 Lê Thánh Tôn, Phường Bến Nghé, Quận 1,\nThành phố Hồ Chí Minh, Việt Nam\nEmail: hello@mythstrip.com\nĐiện thoại: 097 865 7560'

                sender_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
                
                return redirect('subscribe_success')
            else:
                # Người dùng đã đăng ký trước đó
                result = '''
                    <div class="alert alert-danger" role="alert">
                        Email đã được đăng ký, xin vui lòng thử lại!!
                    </div>
                '''
            
    return render(request, 'app/subscribe.html',{
        'result': result,
    })
            


def subscribe_success(request):

    return render(request, 'app/subscribe_success.html')

def contact(request):
    result = ''
    form = FormContact()

    if request.method == 'POST':
        form = FormContact(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Gửi email
            
            company_email = 'thm.myth@gmail.com'
            company_subject = 'Thông báo phản hồi từ khách hàng'
            company_message = f'Có thông tin phản hồi từ khách hàng "{name}"\nEmail: {email}\nSố điện thoại: {phone_number}\nNội dung:\n"{message}"\n\nVui lòng kiểm tra và xử lý.'
            send_mail(company_subject, company_message, settings.EMAIL_HOST_USER, [company_email], fail_silently=False)

            subject = 'Phản hồi liên hệ từ Công Ty Mythstrip'
            message = f'Kính gửi {name},\n\nChúng tôi xin trân trọng gửi lời cảm ơn chân thành nhất tới quý khách hàng đã liên hệ với Công Ty TNHH MTV Du Lịch và Sự Kiện Mythstrip. Chúng tôi rất vui mừng được nhận được sự quan tâm và mong muốn hợp tác từ phía quý khách.\n\nChúng tôi đã nhận được thông điệp của quý khách hàng với nội dung như sau:\n\n"{message}"\n\nChúng tôi đang tiến hành xem xét và xử lý nội dung của quý khách. Đội ngũ chuyên viên của chúng tôi sẽ cố gắng phản hồi lại quý khách hàng trong thời gian sớm nhất có thể.\n\nTrong trường hợp có bất kỳ yêu cầu cụ thể, thắc mắc hoặc điều gì cần được giải đáp thêm, Quý khách hàng có thể liên hệ trực tiếp với chúng tôi qua địa chỉ email hello@mythstrip.com hoặc số điện thoại 097 865 7560. Đội ngũ chăm sóc khách hàng của chúng tôi sẽ sẵn lòng hỗ trợ và giải đáp mọi thắc mắc của Quý vị.\n\nMột lần nữa, chúng tôi chân thành cảm ơn sự quan tâm và ủng hộ từ Quý khách hàng. Mong rằng chúng ta sẽ có cơ hội hợp tác và tạo ra những trải nghiệm du lịch đáng nhớ cùng nhau.\n\nTrân trọng,\n\nCông Ty TNHH MTV Du Lịch Và Sự Kiện Mythstrip\nL17-11, tầng 17 tòa nhà Vincom Center,\n72 Lê Thánh Tôn, Phường Bến Nghé, Quận 1,\nThành phố Hồ Chí Minh, Việt Nam\nEmail: hello@mythstrip.com\nĐiện thoại: 097 865 7560'

            sender_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
            # Lưu thông tin vào database
            form.save()

            result = '''
                <div class="alert alert-success" role="alert">
                    Cảm ơn bạn đã liên hệ với chúng tôi! Chúng tôi sẽ phản hồi lại bạn trong thời gian sớm nhất.
                </div>
            '''
    
    return render(request, 'app/contact.html', {
        'form': form, 
        'result': result,
        })






def packages(request):
    tours = Packages.objects.all().order_by('id')
    

    # search
    products_name = request.GET.get('product_search')
    
    if products_name:
        tours = tours.filter(destination_name__icontains=products_name)
        

    page = request.GET.get('page', 1)
    paginator = Paginator(tours, 6)
    products_pager = paginator.page(page)

    return render(request, 'app/packages.html',{
        'tours': tours,
        'tours': products_pager,
        'products_name': products_name, 
        
    })

def packages_detail(request, tour_id):
    # Lấy thông tin gói tour từ ID
    tour = Packages.objects.get(id=tour_id)
    tours_packages = Packages.objects.all()
    images = PackageImage.objects.filter(package=tour)
    

    # Render template và truyền dữ liệu gói tour vào
    return render(request, 'app/packages_detail.html', {
        'tour': tour,
        'images': images,
        'tours_packages': tours_packages,
        })





def login(request):
    context = {}
    return render(request,'app/login.html', context)






