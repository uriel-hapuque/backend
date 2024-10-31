from reports.serializers import ReportSerializer
from reports.models import Report
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from reports.permissions import IsReportCreator, ReadOnly

class ListCreateReportView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyReportView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsReportCreator | ReadOnly]
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    lookup_url_kwarg='report_id'

