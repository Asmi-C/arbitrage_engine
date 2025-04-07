from django.http import JsonResponse
from rest_framework.views import APIView
from .models import ArbitragePredictor

class ArbitrageAPI(APIView):
    def get(self, request):
        ticker1 = request.GET.get('ticker1', 'PEP')
        ticker2 = request.GET.get('ticker2', 'KO')
        
        data = DataFetcher([ticker1, ticker2]).fetch_realtime()
        signal = PairsTrader().generate_signal(data.iloc[-1])
        
        return JsonResponse({
            "signal": signal,
            "spread": float(data.iloc[-1].mean())
        })