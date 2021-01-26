from app.api.viewset import SchoolViewSet, StudentViewSet, StudentInSchool
from rest_framework_nested import routers

# Define simple router
router = routers.SimpleRouter()
router.register('schools', SchoolViewSet)
router.register('students', StudentViewSet) 

# Define nested router
domains_router = routers.NestedSimpleRouter(router, 'schools', lookup='school')
domains_router.register('students', StudentInSchool, basename='school-student')