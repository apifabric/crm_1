import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CustomerServiceTicket-card.component.html',
  styleUrls: ['./CustomerServiceTicket-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CustomerServiceTicket-card]': 'true'
  }
})

export class CustomerServiceTicketCardComponent {


}