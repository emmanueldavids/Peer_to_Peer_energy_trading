from django.shortcuts import render
from django.contrib import messages

""" This contains all the views methods application and rendering
    the html files as responses.
"""



news = [
    {
        'head': 'Wind Energy Report',
        'image': 's1.jpg',
        'title': 'Renewable Energy',
        'headline': 'Impact of Renewable Energy on Climate Change',
        'message': 'lorem ipsum dolor sit amet, consectetur adip\
                    lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                    lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                    lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                    lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                    lorem ipsum dolor sit amet lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet',

        'source': 'https://google.com/search?q=windenergy'
    },

    {
    'head': 'Solar Energy Report',
    'image': 'solar.jpg',
    'title': 'Renewable Energy',
    'headline': 'Impact of Renewable Energy on Climate Change',
    'message': 'lorem ipsum dolor sit amet, consectetur adip\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet',

    'source': 'https://google.com/search?q=solarenergy'
    },
    {
    'head': 'P2P Energy Report',
    'image': 'p2p.png',
    'title': 'Renewable Energy Trade',
    'headline': 'Impact of Renewable Energy on Climate Change',
    'message': 'lorem ipsum dolor sit amet, consectetur adip\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet\
                lorem ipsum dolor sit amet lorem ipsum dolor sit amet, consectetur adip lorem ipsum dolor sit amet',

    'source': 'https://google.com/search?q=p2penergy'
    }

]

def wallet_details(request):
    """ Here is the landing page of the backend service 
        that shows payments details and trades
    """
    return render(request, 'wallet-info/wallet-details.html', {'message': messages})
    

def trade(request):
    """ This method returns the trade statistics to buy or 
        sell 
    """
    return render(request, 'dashboard/trade.html')


# def alert(request):
#     """ This method returns alerts on the markets trades"""
#     return render(request, 'dashboard/alerts.html')


# def prices(request):
#     """This method returns the price lists on the energy markets"""

#     return render(request, 'dashboard/prices.html')


# def sell_energy(request):
#     """ The sell_energy option for the p2p exchange"""

#     return render(request, 'dashboard/sell-energy.html')


def feeds(request):
    """ Returns the current news feeds from the energy market """
    return render(request, 'dashboard/feeds.html', {'feeds': news})


def wallet(request):
    """ This method returns and render the wallet template """
    return render(request, 'dashboard/wallet.html')


def transactions(request):
    """This method returns and render the transactions template """
    return render(request, 'dashboard/transactions.html')