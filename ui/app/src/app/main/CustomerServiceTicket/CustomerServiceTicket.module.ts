import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CUSTOMERSERVICETICKET_MODULE_DECLARATIONS, CustomerServiceTicketRoutingModule} from  './CustomerServiceTicket-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CustomerServiceTicketRoutingModule
  ],
  declarations: CUSTOMERSERVICETICKET_MODULE_DECLARATIONS,
  exports: CUSTOMERSERVICETICKET_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CustomerServiceTicketModule { }