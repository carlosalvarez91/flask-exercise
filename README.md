Flask exercise
===========
App built in Flask (a Python framework) following the following requirements:

1. Read in the attached file and produce a list sorted by lease amount in ascending order.
2. Display the first 5 results in a table that can then be toggled between ascending/descending value.
3. Allow the user to enter a new entry to the list of mast data. When adding this entry update the frontend to
 display this new entry if it meets the lease amount requirements from point 1.
4. Display the total rent for all items in this list.
5. Create a dictionary containing tenant name and a count of masts for each tenant. Display a list of tenants
currently on show and the count of masts they each have.
NOTE. Treat &quot;Everything Everywhere Ltd&quot; and &quot;Hutchinson3G Uk Ltd&amp;Everything Everywhere Ltd&quot; as
separate entities.
6. List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
This list should use the date format of: DD/MM/YYYY.


Comments
-------------------

> **a)** Missing point 5 and 6.

>**b)** I had to modify the CSV file as there were white spaces at the header, for example: 'Property Name' , so I couldn't call each object from the html inside the table like this: <td> {{obj.property_name}} </ td>
>
>As well I couldn't find the way to delete the '[]' symbols in the header, for example: 'Property Address [1]'.
>
>And along the rows were more commas than they were supposed to be.
>
>**c)** Consider that before this exercise I didn't have any knowledge in Python.



