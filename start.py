# Import appropriate modules from the client library.
from googleads import ad_manager

ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
network_service = ad_manager_client.GetService('NetworkService')

current_network = network_service.getCurrentNetwork()

print(f"encontrada red {current_network['displayName']} ({current_network['networkCode']})")



def main(client):
  # Initialize appropriate service.
  order_service = client.GetService('OrderService', version='v202211')

  # Create a statement to select orders.
  statement = ad_manager.StatementBuilder(version='v202211')

  # Retrieve a small amount of orders at a time, paging
  # through until all orders have been retrieved.
  while True:
    response = order_service.getOrdersByStatement(statement.ToStatement())
    print('response total:')
    print(response)
    if 'results' in response and len(response['results']):
      for order in response['results']:
        # Print out some information for each order.
        print('Order with ID "%d" and name "%s" was found.\n' % (order['id'],
                                                                 order['name']))
      statement.offset += statement.limit
    else:
      break

  print('\nNumber of results found: %s' % response['totalResultSetSize'])


if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  main(ad_manager_client)