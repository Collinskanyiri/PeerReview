import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProjectsComponent } from './components/Projects/projects/projects.component';
import { SignupComponent } from './components/User/signup/signup.component';
import { SigninComponent } from './components/User/signin/signin.component';
import { ProfileComponent } from './components/User/profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    ProjectsComponent,
    SignupComponent,
    SigninComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
