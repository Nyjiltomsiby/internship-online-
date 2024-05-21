from django.contrib import admin
from NEeduapp.models import Course,Tag ,Prerequisite,Learning ,Video
from NEeduapp.models import Course , UserCourse , Tag , Prerequisite , Learning , Video ,Payment,Review,Testimonial
from NEeduapp.models.course import Mentor
from django.utils.html import format_html
# Register your models here.



class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name', 'bio')
    


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin , VideoAdmin]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
   
    

    
    
    list_display = ["name" , 'get_price' , 'get_discount' , 'active']
    list_filter = ("discount" , 'active')

    def get_discount(self , course):
        return f'{course.discount} %'
    
    def get_price(self , course):
        return f'₹ {course.price}'
    
    get_discount.short_description= "Discount"
    get_price.short_description = "Price"

class PaymentAdmin(admin.ModelAdmin):
    model = Payment   
    list_display = [ "order_id" , 'get_user' , 'get_course' , 'status'] 
    list_filter = ["status" , 'course']

    def get_user(self , payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    

    def get_course(self , payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


class UserCourseAdminModel(admin.ModelAdmin):
    model = UserCourse   
    list_display = ['click' , 'get_user' , 'get_course'] 
    list_filter = ['course']

    def get_user(self , usercourse):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")
    
    def click(self , usercourse):
        return "Click to Open"
    

    def get_course(self , usercourse):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{usercourse.course.id}'>{usercourse.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'mentor', 'rating']
    list_filter = ['course', 'mentor']
    search_fields = ['course__name', 'mentor__name']
    list_per_page = 20

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['course', 'text']
    search_fields = ['course__name', 'text']
    list_per_page = 20

    
admin.site.register(Course , CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment , PaymentAdmin)
admin.site.register(UserCourse , UserCourseAdminModel)
admin.site.register(Mentor, MentorAdmin)


