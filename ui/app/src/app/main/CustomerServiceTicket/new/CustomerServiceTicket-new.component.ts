import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CustomerServiceTicket-new',
  templateUrl: './CustomerServiceTicket-new.component.html',
  styleUrls: ['./CustomerServiceTicket-new.component.scss']
})
export class CustomerServiceTicketNewComponent {
  @ViewChild("CustomerServiceTicketForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}