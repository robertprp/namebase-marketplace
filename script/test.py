from namebase_marketplace import marketplace

def should_accept_offer(offerAmount, threshold):
    return float(offerAmount) >= threshold

def get_best_offer(bestBidId, domain_history):
    negotiations = domain_history['negotiations']
    for negotiation in negotiations:
        history = negotiation['history']
        for hist in history['bids']:
            amount = hist['amount']
            id = hist['bidId']
            isAccepted = hist['isAccepted']
            if id == bestBidId and not isAccepted:
                return {"id" : id, "amount" : float(amount)}

    return {}

if __name__ == '__main__':
    cookie= 'your cookie'
    m = marketplace.Marketplace(namebase_cookie=cookie)
    offers = m.get_offers()
    threshold = 8
    for offer in offers:
        ownerId = offer['ownerId']
        history = m.get_offers_domain_history(domainOwnerId=ownerId)
        bestBidId = history['negotiations'][0]['bestBidId']
        if bestBidId:
            best_offer = get_best_offer(bestBidId=bestBidId,
                                        domain_history=history)
            offerAmount = best_offer['amount']
            id = best_offer['id']
            should_accept = should_accept_offer(offerAmount=offerAmount,
                                                threshold=threshold)
            if should_accept:
                res = m.accept_offer(offer_id=id)
