import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css'],
})
export class ProjectsComponent implements OnInit {
  result: Project[] = [];

  project_name: string = '';
  description: string = '';
  project_img: any = '';
  project_url: any = '';

  constructor(private api: ProjectService) {}

  callProjectApi() {
    this.api.getApi().subscribe((result: any) => {
      this.result = result;
      console.log('success', this.result);
    });
  }

  ngOnInit(): void {
    this.callProjectApi();
  }

  postProject() {
    let projectForm = new FormData();
    projectForm.append('project_name', this.project_name);
    projectForm.append('description', this.description);
    projectForm.append('project_img', this.project_img);
    projectForm.append('project_url', this.project_url);
    console.log(projectForm);
    this.api.postProj(projectForm);
  }
}
